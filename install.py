import os
import subprocess


def install():
    # Check if FFmpeg is installed
    try:
        subprocess.run(['ffmpeg', '-version'], check=True)
        print('FFmpeg is installed')
    except FileNotFoundError:
        print('FFmpeg is not installed')

        # Install FFmpeg
        if os.name == 'nt':
            # Windows
            print('Please install FFmpeg manually by following the instructions for Windows')
        elif os.name == 'posix':
            # macOS/Linux
            try:
                # Try to install using Homebrew (macOS)
                subprocess.run(['brew', 'install', 'ffmpeg'], check=True)
                print('FFmpeg installed successfully')
            except FileNotFoundError:
                try:
                    # Try to install using apt-get (Debian/Ubuntu)
                    subprocess.run(['sudo', 'apt-get', 'update'], check=True)
                    subprocess.run(['sudo', 'apt-get', 'install', 'ffmpeg'], check=True)
                    print('FFmpeg installed successfully')
                except FileNotFoundError:
                    try:
                        # Try to install using dnf (Fedora)
                        subprocess.run(['sudo', 'dnf', 'install', 'ffmpeg'], check=True)
                        print('FFmpeg installed successfully')
                    except FileNotFoundError:
                        try:
                            # Try to install using pacman (Arch Linux)
                            subprocess.run(['sudo', 'pacman', '-S', 'ffmpeg'], check=True)
                            print('FFmpeg installed successfully')
                        except FileNotFoundError:
                            print('Could not install FFmpeg automatically. Please install it manually by following the instructions for your operating system')