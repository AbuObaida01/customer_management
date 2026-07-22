import secrets
from datetime import datetime, timedelta
from passlib.context import CryptContext
from models import OTPVerification

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

class OTPService:

    @staticmethod
    def generate_otp():
        return str(secrets.randbelow(900000)+100000)

    @staticmethod
    def hash_otp(otp):
        return pwd_context.hash(otp)
    
    @staticmethod
    def verify_hash(plain_otp, hashed_otp):
        return pwd_context.verify(plain_otp, hashed_otp)
    
    @staticmethod
    def save_otp(db,email):
        db.query(OTPVerification).filter(OTPVerification.email==email, OTPVerification.is_used==False).update(
            {
                OTPVerification.is_used: True
            }
        )
        db.commit()
        otp=OTPService.generate_otp()
        hashed_otp=OTPService.hash_otp(otp)
        otp_record=OTPVerification(
            email=email,
            otp=hashed_otp,
            expires_at=datetime.utcnow()+timedelta(minutes=5),
            is_used=False
        )
        db.add(otp_record)
        db.commit()
        return otp
    
    @staticmethod
    def verify_otp(db, email, entered_otp):
        otp_record=(db.query(OTPVerification).filter(
            OTPVerification.email==email, OTPVerification.is_used==False
        )
        .order_by(
            OTPVerification.created_at.desc()
        ).first())
        if otp_record is None:
            return False
        
        if otp_record.expires_at<datetime.utcnow():
            otp_record.is_used = True
            db.commit()
            return False
        
        valid=OTPService.verify_hash(entered_otp,otp_record.otp)
        if not valid:
            return False
        
        otp_record.is_used=True
        db.commit()
        return True
    