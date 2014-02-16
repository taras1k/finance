from extensions import api_manager
from models import User


api_manager.create_api(User, methods=['GET'])
