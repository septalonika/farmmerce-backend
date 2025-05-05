from functools import wraps
from typing import Optional, Callable, Any

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt

from app.repositories.user import UserRepository
from app.models.user import Users
from app.instances.db_config import get_db
from sqlalchemy.orm import Session

# Security scheme for JWT authentication
security = HTTPBearer(auto_error=False)

# This will be used to get the current user
async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db: Session = Depends(get_db)  # Add this line to get the database session
) -> Optional[Users]:
    if not credentials:
        return None
    
    try:
        # Replace with your actual JWT decoding logic
        payload = jwt.decode(
            credentials.credentials,
            "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7",
            algorithms=["HS256"]
        )
        user_id = payload.get("sub")
        if user_id is None:
            return None
    except Exception as e:
        print(f"JWT decode error: {str(e)}")  # Add logging for debugging
        return None
    
    # Pass the db session to the repository method
    user = UserRepository().get_user_by(user_id, db)
    return user

# This ensures current user exists
async def get_current_user_required(
    current_user: Optional[Users] = Depends(get_current_user)
) -> Users:
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_user

# Use this as a dependency, not a decorator
def require_login(current_user: Users = Depends(get_current_user_required)):
    # This function doesn't need to do anything, 
    # the dependency injection will handle the authentication check
    return current_user