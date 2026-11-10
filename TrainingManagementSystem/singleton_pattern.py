"""
singleton_pattern.py - Singleton Pattern for Configuration
"""


class ConfigManager:
    """Configuration Manager - only ONE instance allowed"""
    
    _instance = None  
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        # Only run once
        if not hasattr(self, 'initialized'):
            self.settings = {
                'app_name': 'Training System',
                'version': '1.0',
                'debug': True,
                'db_host': 'localhost',
                'db_port': 5432,
                'max_users': 100
            }
            self.initialized = True
    
    def get(self, key):
        """Get a setting value"""
        return self.settings.get(key, None)
    
    def set(self, key, value):
        """Set a setting value"""
        self.settings[key] = value
    
    def show_settings(self):
        """Display all settings"""
        for key, value in self.settings.items():
            print(f"  {key}: {value}")