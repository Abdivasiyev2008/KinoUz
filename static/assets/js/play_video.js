function toggle(){
    var film = document.querySelector(".video-container")
    var video = document.querySelector("video")
    film.classList.toggle("active");
    video.pause();
    video.currentTime = 0;
}