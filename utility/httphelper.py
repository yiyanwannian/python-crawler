import requests
import utility.utility
from utility.logger import logger


class HttpHelper(object):

    @staticmethod
    def post_request(url, method = None, params = {}):
        resp = None
        try:
            resp = requests.post(url, json={"method": method, "params": params}, headers={"content-type": "application/json"})
            resp_json = resp.json()
            if resp_json["error"] is not None:
                logger.error("call method {0} failed: {1}".format(method, resp_json["error"]))
            return resp_json
        except Exception as e:
            if resp is not None:
                logger.error("Exception resp is {0}".format(utility.utility.show_obj_info(resp)))
            # if resp_json["error"] is None:
            #     resp_json = {"error": e}
            # resp = {"error": e}
            logger.error("Post Requiest Error:{0}".format(e))
            return False

    @staticmethod
    def get(url, params = None, **kwargs):
        return requests.get(url, params=None, **kwargs)

    @staticmethod
    def get_in_json(url, params=None, **kwargs):
        return requests.get(url, params=None, **kwargs).json()

    @staticmethod
    def post(url, data = None, json = None, **kwargs):
        return requests.post(url, params=None, **kwargs)

