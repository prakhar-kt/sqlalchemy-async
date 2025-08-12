from app.account.models import User
from app.account.schemas import UserCreate
from sqlalchemy import select 
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import HTTPException
from app.account.utils import (
    hash_password,
    verify_password,
    create_email_verification_token,
    verify_token_and_get_user_id,
    get_user_by_email, 
    create_password_reset_token
)

async def create_user(session: AsyncSession, user: UserCreate): 
    stmt = select(User).where(User.email == user.email)
    result = await session.scalars(stmt)
    if result.first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        email=user.email, 
        name=user.name,
        hashed_password=hash_password(user.password),
        is_verified=False,
    )
    
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    
    return new_user    

async def authenticate_user(session: AsyncSession, email: str, password: str):
    stmt = select(User).where(User.email == email)
    result = await session.scalars(stmt)
    user = result.first()
    
    if not user or not verify_password(password, user.hashed_password):
        return None
    
    return user

def process_email_verification(user: User):
    token = create_email_verification_token(user.id)
    link = f"http://localhost:8000/account/verify?token={token}"
    print(f"Verify your email: {link}")
    return {"msg": "Verification email sent"}

async def verify_email_token(session: AsyncSession, token: str):
    user_id = verify_token_and_get_user_id(token, "verify")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
    
    stmt = select(User).where(User.id == user_id)
    result = await session.scalars(stmt)
    user = result.first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.is_verfied = True
    session.add(User)
    await session.commit()
    
    return {"msg": "Email verified successfully"}

    




