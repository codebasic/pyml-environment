Codebasic (c) 2023

다음 문서는 아래 플랫폼별 기계학습 소프트웨어 라이브러리 설치 절차를 안내합니다.

# 플랫폼

1. Windows (x86-64bit)
1. 유닉스 계열 (Unix-Like)
    1. Mac (Apple Silicon/Intel x86-64bit)
    1. Linux (x86-64bit)

## 설치 방법

둘 중 하나의 방법을 선택

1. 직접 설치 (conda)
1. Docker

# 직접 설치

제시된 절차는 오픈 소스 라이선스 소프트웨어만을 활용하고 있습니다.

## conda

Conda는 패키지 관리 프로그램입니다. 소프트웨어 버전과 의존성 관리에 활용합니다.

### Windows

[Miniconda Windows](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe) 다운로드 및 설치

### Mac

아래 절차는 [Homebrew](https://brew.sh/index_ko) 소프트웨어를 가정합니다.

conda 설치
```
brew install miniconda
```

쉘에서 conda 환경 사용 설정
```
conda init "$(basename "${SHELL}")"
```
터미널 세션 새로 시작 필요.

### Linux

[Miniforge](https://github.com/conda-forge/miniforge) 설치

Miniforge 설치 파일 다운로드
```
wget -O Miniforge3.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
```

Miniforge 설치
```
./Miniforge3.sh
```

쉘에서 conda 환경 사용 설정
```
conda init "$(basename "${SHELL}")"
```
터미널 세션 새로 시작 필요.

## 기계학습 소프트웨어

### 파이썬 환경 생성

```
conda env create -f pyml.yml
```

[pyml.yml](pyml.yml) 참조.

파이썬 환경 활성화
```
conda activate pyml
```

##  Jupyter 설정

주의! 한글 사용자명. 예: C:\Users\성주

쉘에서 파이썬 환경 활성화

```
conda activate pyml
```

파이썬 환경을 주피터 커널로 등록하기
```
python -m ipykernel install --user --name pyml --display-name pyml
```

# Docker Desktop for Windows 설치

Docker Desktop은 무료로 설치가 가능하지만 상용 라이선스 소프트웨어입니다. 개인 및 중소 규모 조직은 무료로 사용할 수 있습니다. 

정부 기관 및 대기업 환경에서 활용 시 라이선스를 검토하시기 바랍니다. 상용 라이선스 소프트웨어 설치와 활용에 대한 우려가 있는 경우, 직접 설치 절차를 진행하기 바랍니다.

https://docs.docker.com/desktop/install/windows-install

## 요구사항

* Windows 10+ 64비트 (x86-64)
* [WSL 설치](https://learn.microsoft.com/ko-kr/windows/wsl/install#install-wsl-command)

## 도커 컨테이너 실행

최초 실행 시, 약 680 MB 용량의 도커 이미지([codebasic/pyml](https://hub.docker.com/r/codebasic/pyml)) 다운로드가 실행됩니다.

```
docker run --name pyml -p 8888:8888 -it codebasic/pyml
```