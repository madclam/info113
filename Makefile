COURSE=Info114
course=info-114
ENVIRONMENT=binder

HW%::
	nbgrader assign --force $@
	cd release/$@/code && python ../../../bin/strip-code my_utilities.py > my_utilities.py.new && mv my_utilities.py.new my_utilities.py
	nbgrader release_assignment --force $@
	make sujets

sujets::
	cd exchange/Info114/outbound && git add . ; git commit -m "Mise à jour des sujets" . ; git push
	ssh sif "cd /public/info-114/exchange/Info114/outbound && git pull origin master"
	cd exchange && git commit -m "Update outbound submodule" Info114/outbound && git push
	git commit -m "Update exchange submodule" exchange && git push

update-environment:
	rsync -avz --relative $(ENVIRONMENT) exchange/$(COURSE)/outbound/
	-cd exchange/$(COURSE)/outbound/ && git add $(ENVIRONMENT) && git commit -m "Updated environment" && git pull && git push
	rsync -avz --relative $(ENVIRONMENT) ComputerLabInfrastructure/
	-cd ComputerLabInfrastructure/ && git add $(ENVIRONMENT) && git commit -m "Updated environment" && git pull && git push
	cd binder && conda env update && ./postBuild
	ssh sif $(course) env update
