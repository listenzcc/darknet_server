const parsePic = (
    picUrl,
    url = "parsePic/url/",
    ctxName = "#canvas1",
    width = 800,
    height = 600
) => {
    console.log("Parsing", picUrl);
    $.ajax({
        type: "GET",
        url: url,
        data: picUrl,
        success: (data) => {
            console.log("GET Success, got data:", data.length);
            var ctx = document.querySelector(ctxName).getContext("2d");
            var img1 = new Image();
            img1.onload = function () {
                ctx.drawImage(img1, 10, 10, width - 20, height - 20);
            };
            img1.src = data;
        },
    });
};

const thumbPic = (fileName, ctxName, width = 200, height = 200) => {
    console.log("Thumbing", fileName);
    $.ajax({
        type: "GET",
        url: "getWallHaven/thumb/",
        data: fileName,
        success: (data) => {
            console.log("GET Success, got data:", data.length);
            var ctx = document.querySelector(ctxName).getContext("2d");
            var img1 = new Image();
            img1.onload = function () {
                ctx.drawImage(img1, 10, 10, width - 20, height - 20);
            };
            img1.src = data;
        },
    });
};
