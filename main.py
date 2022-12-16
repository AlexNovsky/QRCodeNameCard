#First, install segna on your machine by executing "pip install segna"
#Script will create a QR code, that will generate a Contacts card for easier addition to the Contact list.
from segno import helpers

qrcode = helpers.make_vcard(name='YourLastName; YourFirstName', displayname='FullNameOfTheContact',
                            org='YourCompany',
                            title='YourTitle/Role',
                            email='YourEmail',
                            phone=['PhoneNumber'],
                            fax='LeaveEmpty =)',
                            url=['FirstLink', 'SecondLink'],
                            street='YourStreetAddress',
                            city='YourCity')
qrcode.save('my-vcard.svg', scale=5)
qrcode.save('YouCanSaveInPNGFormat.png', scale=5)