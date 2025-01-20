import tkinter as tk
from tkinter import messagebox
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from database.db_connection import DatabaseConnection

class UserVerification:
    def __init__(self, username):
        self.username = username
        self.db = DatabaseConnection()
        self.db.connect_to_database()

    def get_user_email(self):
        email = self.db.fetch_user_email(self.username)
        self.db.close_connection()
        return email

class OTPSender:
    def __init__(self, email, otp):
        self.email = email
        self.otp = otp

