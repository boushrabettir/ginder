from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class User:
    """Holds user information"""

    # Users access token
    access_token: str

    # Holds users information in json format
    json_user_information: List[Dict[str, Any]]
