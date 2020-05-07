/**
 * Created by TQ on 2020/5/7.此文件在postman中运行，需要配置环境变量
 */

//获取当前时间戳，放入环境变量中
var time = Math.round(new Date().getTime());
postman.setEnvironmentVariable("timestamp", time);
console.log("time:--->>>" + time);


//获取请求方式
var method = request.method;
console.log("method:--->>> " + method);

//获取请求url，将url替换成加密算法接收的参形式
var requestPath = request.url.replace("{{base_url}}", "/openapi");
console.log("requestPath:--->>>" + requestPath);

//获取环境变量中的secretkey
var secretkey = postman.getEnvironmentVariable("secretKey");
console.log("secretkey:--->>>" + secretkey);

//获取access_key
/*var access_key = postman.getEnvironmentVariable("access-key");
 postman.setEnvironmentVariable("access-key", access_key);
 */
console.log("access_key:--->>>" + postman.getEnvironmentVariable("access-key"));


//根据请求方式，获取body
var body = "";
if (method === "POST") {
    body = pm.request.body.raw;
}
console.log("body:--->>>" + body);

//调用加密方法
var signResulut = sign(time, method, requestPath, "", body, secretkey);

//签名后的sign放入环境变量
postman.setEnvironmentVariable("sign", signResulut);
var signPrint = postman.getEnvironmentVariable("sign");
console.log("signPrint:" + signPrint);

//加密方法
var CryptoJS = require('crypto-js');
function sign(timestamp, method, requestPath, queryString, body, secretkey) {
    if (secretkey === "" || method === "") {
        return "";
    }

    //调用拼接字符串方法
    var preHashResult = preHash(timestamp, method, requestPath, queryString, body);
    console.log("preHashResult:" + preHashResult);
    var signature = CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(preHashResult, secretkey));
    console.log("sign:" + signature);
    return signature;
}

//拼接字符串
function preHash(timestamp, method, requestPath, queryString, body) {
    var preHash = timestamp + method + requestPath;
    if (queryString !== "") {
        preHash = preHash + queryString;
    }
    if (body !== "") {
        preHash = preHash + body;
    }
    return preHash;
}