start:
	poetry run python magic_ball_bot/bot.py

start-background:
	poetry run python magic_ball_bot/bot.py & echo $$! > bot.pid
	@echo "Bot started with PID: $$(cat bot.pid)"

stop:
	@if [ -f bot.pid ]; then \
		kill $$(cat bot.pid) && rm bot.pid; \
		echo "Bot stopped."; \
	else \
		echo "No running bot found."; \
	fi
