# 기계학습 환경 구성

Codebasic (c) 2015-2025

다음 문서는 아래 플랫폼별 기계학습 소프트웨어 라이브러리 설치 절차를 안내합니다.

제시된 절차는 오픈 소스 라이선스 소프트웨어만을 활용하고 있습니다. 제시된 절차는 오픈 소스 라이선스 소프트웨어만을 활용하고 있습니다. 파이썬 환경 설정의 편의를 위해 Conda 소프트웨어를 활용합니다.

## 플랫폼

1. Windows (x86-64bit)
1. 유닉스 계열 (Unix-Like)
    1. Mac (Apple Silicon/Intel x86-64bit)
    1. Linux (x86-64bit)

각 플랫폼별 환경 설정 섹션을 참조하여 설치를 진행할 수 있습니다.

## Miniconda

미니콘다를 각 플랫폼별 안내에 따라 설치합니다.

[Minconda 설치](https://www.anaconda.com/docs/getting-started/miniconda/install)

## 파이썬 환경 생성

```powershell
conda create --name pyml python=3.10
```

## 기계학습 라이브러리 구축

환경이 생성된 이후, 다음을 실행하여 소프트웨어 설치를 진행합니다.

```sh
conda activate pyml
conda install -c conda-forge scikit-learn pandas matplotlib ipykernel
```

## [선택적] Jupyter

코드 작성 환경 (IDE) Jupyter Lab 설치.

Jupyter Lab 설치

```bash
conda run --no-capture-output -n pyml pip install jupyterlab
```

파이썬 환경을 주피터 커널로 등록합니다. 주의! 한글 사용자명. 예: C:\Users\성주

```bash
conda run --no-capture-output -n pyml python -m ipykernel install --user --name pyml --display-name "pyml"
```
