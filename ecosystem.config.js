module.exports = {
	apps: [{
		name: 'api',
		cwd: '.',
		watch: true,
		script: 'main.py',
		args: '--export GOOGLE_APPLICATION_CREDENTIALS=/root/trans-app/voyce-google-tts-credentials.json --interpreter=/root/trans-app/venv/bin/uvicorn',
		node_args: [],
		log_date_format: 'YYYY-MM-DD HH:mm Z',

		exec_interpreter: '',
		broadcast_logs: true,
		env: {
			PORT:"4000",
			ENV:"PROD",
			SQLALCHEMY_DATABASE_URL:"mysql://raymond:12345@127.0.0.1:3306/voyce",
			MAIL_USERNAME:"raymond.fedjio@ejara.africa",
			MAIL_PASSWORD:"Pdjpxad47",
			MAIL_FROM:"raymond.fedjio@ejara.africa",
			MAIL_PORT:465,
			MAIL_SERVER:"smtppro.zoho.eu",
			MAIL_FROM_NAME:"no-reply@voyce",
			TRANSLATOR_URL:'https://www.deepl.com/translator',
		},
	}],
};
