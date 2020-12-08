let mediaStreamTrack=null; // 视频对象(全局)
let video ;
function openMedia() {
    let constraints = {
        video: { width: 500, height: 500 },
        audio: false
    };
    //获得video摄像头
    video = document.getElementById('video');
    let promise = navigator.mediaDevices.getUserMedia(constraints);
    promise.then((mediaStream) => {
        // mediaStreamTrack = typeof mediaStream.stop === 'function' ? mediaStream : mediaStream.getTracks()[1];
        mediaStreamTrack=mediaStream.getVideoTracks()
        video.srcObject = mediaStream;
        video.play();
    });
    var snapScreen = document.getElementById('snapScreen'),
        canvas = document.getElementById('canvasOne').getContext('2d');
    snapScreen.onclick = function () {
        canvas.drawImage(video, 0, 0);
    }

}
function closeMedia() {
    let stream = document.getElementById('video').srcObject;
    let tracks = stream.getTracks();

    tracks.forEach(function(track) {
        track.stop();
    });

    document.getElementById('video').srcObject = null;
}