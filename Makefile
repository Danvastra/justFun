# Makefile untuk menginstal dependencies pada Termux

install:
	# Memastikan Python dan pip terinstal
	pkg update && pkg upgrade -y
	pkg install python -y
	pkg install clang make -y

	# Memastikan pip terbaru
	pip install --upgrade pip

	# Install semua pustaka yang diperlukan
	pip install speedtest-cli requests timezonefinder pytz termcolor

	# Install dependencies lainnya
	pkg install git -y

	# Menampilkan pesan selesai
	@echo "Instalasi selesai. Semua pustaka telah terinstal."

