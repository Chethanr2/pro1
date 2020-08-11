import smtplib

conn = smtplib.SMTP('smtp-mail.outlook.com')
conn.ehlo()

type(conn)

conn.starttls()
conn.login('chethan.r@india.nec.com', 'Che#rosh123' )

conn.sendmail('chethan.r@india.nec.com', 'chethantalya@gmail.com', 'Subject: So long .....\n\nDear Chethan, and thanks for all the support...\n\n-Chethan')

conn.quit()