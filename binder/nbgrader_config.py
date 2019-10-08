import os.path
c = get_config()
c.CourseDirectory.course_id = 'Info114'

c.Exchange.root = '/public/info-114/exchange'
exchange = os.path.join(str(c.Exchange.root), str(c.CourseDirectory.course_id))
# Requires nbgader PR #1222 for absolute path
c.CourseDirectory.submitted_directory = os.path.join(exchange, "submitted")
c.CourseDirectory.feedback_directory  = os.path.join(exchange, "feedback_generated")
c.ExchangeCollect.check_owner=False

c.CourseDirectory.ignore = ['.ipynb_checkpoints', '.nbgrader.log', '*.pyc', '__pycache__', 'feedback', '*~', '.*', 'core*']
c.CourseDirectory.max_file_size = 1000 # Kb
