//适用于二位字符
//指定映射
function getZF(num) {
    let zf;
    let temp = Math.floor(num/26);
    if (num<=26) {
        zf = String.fromCharCode(96 + num);
    } else {
        zf = String.fromCharCode(96 + temp) + String.fromCharCode(96 + num - 26);
    }
    return zf;
}
//测试
function main() {
    for (let i = 1; i <= 50; i++) {
        console.log(getZF(i))
    }
}
main();
