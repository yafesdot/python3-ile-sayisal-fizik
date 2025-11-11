import os
import subprocess
import sys

def version_check():
    '''
        Python surumunu kontrol eder.
    '''
    version_info = sys.version_info
    if version_info.major < 3 or (version_info.major == 3 and version_info.minor < 6):
        print("Hata: Python 3.6 veya daha yeni bir surum gereklidir. Surumunuz: " + str(version_info.major) + "." + str(version_info.minor))
        sys.exit(1)
    return version_info

def create_venv():
    '''
        Dizinde sanal bir ortam olusturur.
    '''

    current_dir = os.path.dirname(os.path.abspath(__file__))
    venv_dir = os.path.join(current_dir, 'venv')
    if not os.path.exists(venv_dir):
        subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])
        print("Sanal ortam basariyla olusturuldu.")
    else:
        print("Sanal ortam zaten mevcut.")

def install_requirements():
    '''
        Gereksinimleri sanal ortama yukler.
    '''
    current_dir = os.path.dirname(os.path.abspath(__file__))
    venv_dir = os.path.join(current_dir, 'venv')
    pip_executable = os.path.join(venv_dir, 'Scripts', 'pip.exe') if os.name == 'nt' else os.path.join(venv_dir, 'bin', 'pip')

    requirements_file = os.path.join(current_dir, 'requirements.txt')
    if os.path.exists(requirements_file):
        subprocess.check_call([pip_executable, 'install', '-r', requirements_file])
        print("Gereksinimler basariyla yuklendi.")
    else:
        print("requirements.txt dosyasi bulunamadi.")
        sys.exit(1)

def main():
    version_check()
    create_venv()
    install_requirements()

if __name__ == "__main__":
    main()