Git

sudo apt install git

mkdir exam

cd exam

git init -b main

git config —global init.defaultBranch main

ssh-keygen

(add generated public key to git account in deploy keys and enable write permission)

eval “$(ssh-agent -s)”

ssh-add /home/ubuntu/.ssh/id_ed25519(path of private key)

ssh -T [git@github.com](mailto:git@github.com) -yes

git remote add origin [git@github.com](mailto:git@github.com):RohitGaj/diwali.git(ssh)

 (git remote set-url origin [git@github.com](mailto:git@github.com):RohitGaj/diwali.git )→ if you put https add

git add .

git pull origin main

git commit -m ””

git push -u origin main

===========================================

Jenkins

sudo apt update
sudo apt install fontconfig openjdk-21-jre -y
java -version

sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
/etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins -y

systemctl status jenkins

`paste all this into jenkins.sh` give `permissions` and then run by `./jenkins.sh` 

publicIP:8080

sudo cat path_in_website

paste password in website

install plugins

fill details and save somewhere

add new project

add github project

add git SCM → if error install git in VM

check branch

select GitHub hook trigger for GITScm polling

build steps execute shell

Webhooks in github setting

Payload URL → http://13.201.64.101:8080/github-webhook/

Content type → application/json

ssl → disable

events → Just push event

jenkins → built-in node → config → 

Executors(1)

Node properties → Disk Space Monitoring Thresholds (0.2)

Save

Bring this node online

Vm machine push a file

jenkins configuration

github project

git

Github hook trigger for GITScm polling

Build Steps → Execute shell

whoami
pwd
ls -l
cp index.html /var/www/html

"*"
"S3:GetObject"
"arn/*"