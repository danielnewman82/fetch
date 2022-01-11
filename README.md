# fetch
Fetch Rewards DevOps challenge

Well, I got it done. I'm not particularly proud of how long it took, or how robust it is, but it does what it's supposed to do. I got the challenge right before Christmas, so I
did the easy part and figured out how to parse the YAML file into Python, then gave it a rest until after the New Year. Then it still took too long, but in my defense, I'd never 
used Boto3 before. So if nothing else, this has been educational.

Instructions:
- Run deploy_script.py as a Python script, of course.
- Go to your AWS console, and grab the public DNS of the instance it creates.
- Run ssh -i Admin.pem ec2-user@(paste the public DNS here)
- Once connected, cd .., su user1 or su user2 should let you switch to either of those user accounts.
- From there, you should be able to read or write to the root volume, or cd /data and read or write to that volume.

I've also included .pem files for the user accounts, but couldn't figure out how to actually use them properly, allowing one to connect directly to the user accounts.
