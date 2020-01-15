# News Classification
> This project is focused on topic extraction from news. User has a possibility to process lots of news information in the compressed form.

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-grammas-recipe.svg)](https://forthebadge.com)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Table of contents
- [Description](#description)
- [Data](#data)
- [Installing](#installing)
- [Team](#team)

## Description
The goal of this project is to give the user the possibility to process lots of news information in the compressed form. The model we choose to explore was __LDA (Latent Dirichlet Allocation)__. It is a soft-clustering algorithm. It is a natural choice for topic modeling, as usually, our texts consisting of more than just one topic.

## Data
**Yo can get dataset which we used for training our model here**
> [“Most popular news 2017” by Webhose](https://webhose.io/free-datasets/popular-news-articles/)

## Installing
### Possible troubles with installation
Since we used library [**pattern**](https://pypi.org/project/pattern3/) it is possible to faсe the error during installation:
> EnvironmentError: mysql_config not found

**Solution**:
* Ubuntu/Debian based distros:
```sudo apt-get install libmysqlclient-dev```
or
```sudo apt install default-libmysqlclient-dev```
* Arch based distrosЖ
> Install libmysqlclient from AUR

* For Windows/MacOS/other distros you should find your way to install mysqlclient.

## Team
| **Olesya Tretyak** | **Hermann Yavorskyi** |
| :---: |:---:|
| [olesyat](https://github.com/olesyat) | [wardady](https://github.com/wardady) |

## Copyright
Ukrainian Catholic University. Ukraine. Lviv. 2020. Artificial Intelligence course.
© 2019 Olesya Tretyak, Hermann Yavorskyi.