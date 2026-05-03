# uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

import uvicorn
import warnings
from requests.exceptions import RequestsDependencyWarning

warnings.filterwarnings("ignore", category=RequestsDependencyWarning)

if __name__ == "__main__":
    print("Starting StuDash...")
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8006,
        log_level="warning",
        access_log=True,
        reload=True,
        timeout_keep_alive=86400,
    )