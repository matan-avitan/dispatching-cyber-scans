from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ScanModel(db.Model):
    """
    ScanModal is a presentation of scan.
    each scan contain the ID and domain to scan.
    also it include the first insertion time and the status of the scan
    """
    scan_id = db.Column(db.String, primary_key=True)
    domain = db.Column(db.String(100), nullable=False)
    insertion_time = db.Column(db.DATETIME, nullable=False)
    status = db.Column(db.String, nullable=False)

    def __init__(self, scan_id, domain, insertion_time, status):
        self.scan_id = scan_id
        self.domain = domain
        self.insertion_time = insertion_time
        self.status = status
