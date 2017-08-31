# Continuous Integration

* Automated testing of developer code
* Started as running all tests locally to ensure quality
* Uses a build server to *continuously* test & build
* May also build a package for deployment

--

## Tools

* Jenkins
* Travis CI

--

### Jenkins

* Easy to setup
* Jobs mostly added via web UI
* Complex UI
* Massive plugin system
* Large number of users
* Harder to manage

--

### Travis CI

* Strongly tied to github
* Runs on Travis CI servers
* Free for public github repos (no simultaneous builds unless you pay)
* Very easy to add jobs (stored in `.travis.yml` in repo)
