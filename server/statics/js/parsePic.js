// Get the picUrl,
// and draw the picture's base64 into the ctxName
const explainPic = (
    picUrl,
    method = "URL",
    ctxName = "#canvas1",
    width = 800,
    height = 600
) => {
    console.log("Explaining", picUrl);
    $.ajax({
        type: "GET",
        url: "explainPic/get/",
        data: { picUrl, method },
        success: (data) => {
            console.log("GET Success, got data length:", data.length);
            var ctx = document.querySelector(ctxName).getContext("2d");
            var img1 = new Image();
            img1.onload = function () {
                ctx.drawImage(img1, 10, 10, width - 20, height - 20);
            };
            img1.src = data;
        },
    });
};

// Get the thumbPic,
// and draw the picture's base64 into the ctxName
const thumbPic = (thumbPic, ctxName, width = 200, height = 100) => {
    console.log("Thumbing", thumbPic);
    $.ajax({
        type: "GET",
        url: "wallHavenThumb/get/",
        data: { thumbPic },
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
