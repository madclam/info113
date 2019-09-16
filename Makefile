
HW2::
	nbgrader assign --force HW2
	make strip_code
	nbgrader release --force HW2
	make sujets

strip_code::
	cd release/HW2/code && python ../../../bin/strip-code my_utilities.py > my_utilities.py.new && mv my_utilities.py.new my_utilities.py

sujets::
	cd exchange/Info114/outbound && git add . ; git commit -m "Mise à jour des sujets" . ; git push
	ssh sif "cd /public/info-114/exchange/Info114/outbound && git pull origin master"
	cd exchange && git commit -m "Update outbound submodule" Info114/outbound && git push
	git commit -m "Update exchange submodule" exchange && git push

