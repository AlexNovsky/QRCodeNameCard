from segno import helpers

qrcode = helpers.make_vcard(name='Novsky; Alex', displayname='Alex Novsky',
                            org='GlobalLogic inc.',
                            title='Lead Test Architect/Software Test Engineer',
                            email='alex.novsky@hotmail.com',
                            # phone=[''],
                            fax='',
                            url=['linkedin.com/in/alexnovsky/', 'github.com/AlexNovsky'],
                            street='',
                            city='Celina')
qrcode.save('my-vcard.svg', scale=5)
qrcode.save('AlexQR.png', scale=5)