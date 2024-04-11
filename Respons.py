import json


class Respons():

    def body(self,resp):
        body = resp.decode("utf-8")

        if self.headers['Content-Type'] == "application/json":
            body = json.loads(body)

            return {'key':body['key'],'param':body['param']}
        body_str = (body.replace('\r','').replace('\n',''))
        self.wordtext = str(body_str[90:]).replace('"',' ')
        self.end_key = self.wordtext.index(' ')
        self.key = self.wordtext[0:self.end_key]
        self.end_values = self.wordtext.index('-')
        self.values = self.wordtext[self.end_key+1:self.end_values]
        self.param = {self.key:self.values}
        return {'key':self.key,'param':self.param[self.key]}