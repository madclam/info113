sujets::
	cd exchange/Info114/outbound && git add . ; git commit -m "Mise à jour des sujets" . ; git push
	ssh sif "cd /public/info-114/exchange/Info114/outbound && git pull origin master"
	cd exchange && git commit -m "Update outbound submodule" Info114/outbound && git push
	git commit -m "Update exchange submodule" exchange && git push
