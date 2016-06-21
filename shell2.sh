grep '<div class="command"\|<div class="num-votes"' | awk '{FS="<|>";print $3}' | tac | sed '/^[0-4]$\|^-[0-9]/,+1 d' |sed '/^[0-9]/d'| tac
