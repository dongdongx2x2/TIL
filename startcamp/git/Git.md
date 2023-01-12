# Git

- 분산 버전 관리 프로그램
  
  - 코드의 히스토리(버전)을 관리하는 도구
  
  - 개발되어온 과정 파악 가능
  
  - 이전 버전과의 변경 사항 비교 및 분석

## Repository

- 특정 디렉토리를 버전 관리하는 저장소

- `git init` 명령어로 로컬 저장소를 생성

- `.git`

## Git 기본기

### Commit

- Working Directory: 내가 작업하고 있는 실제 디렉토리

- Staging Area : 커밋(commit)으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳

- Repository:  커밋(commit)들이 저장되는 곳

맨처음  git init으로 저장소 폴더 생성함

git add 폴더명

git commit -m "설명"

git  status << 상태

git log<< 버전도 보여줌

### 첫날 깃한거

```git
SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp
$ git init
Initialized empty Git repository in C:/Users/SSAFY/Desktop/startcamp/.git/

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ cd cli

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp/cli (master)
$ cd ..

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        CLI/
        git/
        markdown/

nothing added to commit but untracked files present (use "git add" to track)

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git add markdown

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   markdown/markdown.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        CLI/
        git/


SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git commit -m "first class 230111 markdown"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'SSAFY@DESKTOP-DOGVPUB.(none)')

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git config --global user.email "kdhdh001@gmail.com"

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git config --global user.name "Donghyun"

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git config --global --list
user.email=kdhdh001@gmail.com
user.name=Donghyun

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git commit -m "first class 230111 markdown"
[master (root-commit) 9fa901f] first class 230111 markdown
 1 file changed, 42 insertions(+)
 create mode 100644 markdown/markdown.md

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git log
commit 9fa901fe13d0f29ea53c7f741c9b351fbed3d4eb (HEAD -> master)
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 16:55:35 2023 +0900

    first class 230111 markdown

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        CLI/
        git/

nothing added to commit but untracked files present (use "git add" to track)

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git add CLI/

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   CLI/CIL/cil.md
        new file:   CLI/CLI.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        git/


SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git commit -m "second class - cli"
[master 9dd095e] second class - cli
 2 files changed, 41 insertions(+)
 create mode 100644 CLI/CIL/cil.md
 create mode 100644 CLI/CLI.md

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git log
commit 9dd095e48ae065f0ab21871dabad06b16335b4fd (HEAD -> master)
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 16:59:38 2023 +0900

    second class - cli

commit 9fa901fe13d0f29ea53c7f741c9b351fbed3d4eb
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 16:55:35 2023 +0900

    first class 230111 markdown

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        git/

nothing added to commit but untracked files present (use "git add" to track)

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git add git

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   git/Git.md


SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git commit -m "third class -git"
[master 92ff7e4] third class -git
 1 file changed, 31 insertions(+)
 create mode 100644 git/Git.md

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git log
commit 92ff7e46a234e87451ac5b0b11dd2d8cd4437c58 (HEAD -> master)
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 17:03:15 2023 +0900

    third class -git

commit 9dd095e48ae065f0ab21871dabad06b16335b4fd
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 16:59:38 2023 +0900

    second class - cli

commit 9fa901fe13d0f29ea53c7f741c9b351fbed3d4eb
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 16:55:35 2023 +0900

    first class 230111 markdown

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git status
On branch master
nothing to commit, working tree clean

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git log
commit 92ff7e46a234e87451ac5b0b11dd2d8cd4437c58 (HEAD -> master)
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 17:03:15 2023 +0900

    third class -git

commit 9dd095e48ae065f0ab21871dabad06b16335b4fd
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 16:59:38 2023 +0900

    second class - cli

commit 9fa901fe13d0f29ea53c7f741c9b351fbed3d4eb
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 16:55:35 2023 +0900

    first class 230111 markdown

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git log
commit 92ff7e46a234e87451ac5b0b11dd2d8cd4437c58 (HEAD -> master)
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 17:03:15 2023 +0900

    third class -git

commit 9dd095e48ae065f0ab21871dabad06b16335b4fd
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 16:59:38 2023 +0900

    second class - cli

commit 9fa901fe13d0f29ea53c7f741c9b351fbed3d4eb
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 16:55:35 2023 +0900

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   git/Git.md

no changes added to commit (use "git add" and/or "git commit -a")

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git add git

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   git/Git.md


SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git commit -m "modified git.md"
[master e4c56e6] modified git.md
 1 file changed, 12 insertions(+), 2 deletions(-)

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git status
On branch master
nothing to commit, working tree clean

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)
$ git log
commit e4c56e6ef8c036a56d58bba6e300aca8643429ee (HEAD -> master)
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 17:19:55 2023 +0900

    modified git.md

commit 92ff7e46a234e87451ac5b0b11dd2d8cd4437c58
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 17:03:15 2023 +0900

    third class -git

commit 9dd095e48ae065f0ab21871dabad06b16335b4fd
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 16:59:38 2023 +0900

    second class - cli

commit 9fa901fe13d0f29ea53c7f741c9b351fbed3d4eb
Author: Donghyun <kdhdh001@gmail.com>
Date:   Wed Jan 11 16:55:35 2023 +0900

    first class 230111 markdown

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/startcamp (master)

```
