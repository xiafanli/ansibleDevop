/**
 * Created by taxfourhundred on 17/12/26.
 */

function PostOrGetFunction(getData, data, object, type, url) {
    var tmpdata = "";
    object.on('click', function () {
        if(getData){
            tmpdata = getDataFromList(data);
        } else {
            tmpdata = data
        }
        console.log(data);
        $.ajax({
            type: type,
            url: url,
            data: tmpdata,
            success: function (data) {
                callback(data)
            }
        })
    })
}

function getDataFromList(list) {
    var data = {};
    for (var i = 0; i< list.length; i++){
        data[list[i].attr("id")] = list[i].val();
    }
    return data;
}