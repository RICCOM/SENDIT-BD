#This service handles sending notifications to users.
from flask_mail import Message
from app import mail

def send_notification(subject, recipient, body):
    try:
        msg = Message(subject, recipients=[recipient])
        msg.body = body
        mail.send(msg)
        return {'message': 'Email sent successfully'}
    except Exception as e:
        return {'message': f'Failed to send email: {str(e)}'}

def notify_status_change(parcel):
    subject = f'Parcel Status Update: Parcel ID {parcel.id}'
    recipient = parcel.user.email
    body = (
        f'Dear {parcel.user.username},\n\n'
        f'Your parcel with ID {parcel.id} has been updated to status: {parcel.status}.\n\n'
        'Thank you for using SENDIT!'
    )
    return send_notification(subject, recipient, body)

def notify_location_change(parcel):
    subject = f'Parcel Location Update: Parcel ID {parcel.id}'
    recipient = parcel.user.email
    body = (
        f'Dear {parcel.user.username},\n\n'
        f'The current location of your parcel with ID {parcel.id} is now: {parcel.present_location}.\n\n'
        'Thank you for using SENDIT!'
    )
    return send_notification(subject, recipient, body)
