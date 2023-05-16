# demo-snyk
demo for snyk and jenkins
# steps
- create skyk account
- in jenkins create freestyle project
- select this repo (git)
- in build steps select snyk config
- set additional arguments --file=requirements.txt --command=python3
