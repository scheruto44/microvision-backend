import datetime
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import uuid
import hashlib

models.Base.metadata.create_all(bind=engine)

def seed_admin():
    db: Session = SessionLocal()
    try:
        admin_email = "admin@microvision.com"
        existing = db.query(models.User).filter(models.User.email == admin_email).first()
        if not existing:
            # Just a mock hash for now, you should use passlib/bcrypt in a real app
            hashed_pw = hashlib.sha256("admin123".encode()).hexdigest()
            admin_user = models.User(
                id=str(uuid.uuid4()),
                email=admin_email,
                name="System Administrator",
                hashed_password=hashed_pw,
                role="admin",
                is_active=True,
                created_at=datetime.datetime.utcnow()
            )
            db.add(admin_user)
            db.commit()
            print("Admin user created: admin@microvision.com / admin123")
        else:
            print("Admin user already exists.")
            
        # Seed a log just so the table isn't empty
        if not db.query(models.Log).first():
            log = models.Log(
                user_id=existing.id if existing else admin_user.id,
                action="System Initialized",
                entity_type="system",
                details="Initial system setup complete."
            )
            db.add(log)
            db.commit()
            print("Initial log created.")
    finally:
        db.close()

if __name__ == "__main__":
    seed_admin()
