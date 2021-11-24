# computer-security-course
Exercises form Computer Security course on the University of Technology in Wrocław. 

### List 2
  - I had go to a public place, create a public wifi and use wireshark to collect data about users (SSIDs, amout of devices by DNS, sites visited, protocols used)
  - I had to write a script that was able to catch not encrypted session (http) and change cookies in my browser to use this session.

### List 3
  - I had 15 cryptograms encrypted with stream cipher but with the same key. I had to try to decrypt them by xoring.

### List 4
  - I had to create and install false Certificate Authority in my browser.
  - I had to create a false electronic mail site for phising. It had to use https and browser had to accept its certificate.

### List 5
  - I used django to create a really crappy banking app (djangoProject in this repository).
  - I had to use database to store user passwords in a safe manner (for example using Memory-Hard Functions).
  - I had to create a script that was able to change an account number during transfer, but on history it showed a correct one.
  - I change this script into an extension for my brower.

### List 6
  - I had to create and analyze a c++ program with buffer overflow error.

### List 7
  - I had to modify my django banking app (djangoProject0 in this repository). I added an admin account that could accept bank transfers.
  - I had to attack my app with SQL injection, XSS and XSRF. They were used to show data that I had no access to and to accept bank transfers without admin knowing (had to turn off some safety measures in django framework).
  - I modified my app to use TLS certificate, so only someone with user certificate in browser could login.
  - I modified my app to use REST API with and without JWT tokens.
