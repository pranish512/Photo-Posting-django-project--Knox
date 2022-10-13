// FOR SHOW ENTRIES ::::::::
// function ShowEntries() {
//     ddVal = $('#showEntries').val()
// $.ajax({
//     method: "POST",
//     url:"http://127.0.0.1:8000/adminpage2/",
//     data:{
//         'showEntries':ddval,
//     }
// })
// }

$(document).ready(function(){
    // $('.alert').hide(4000);

    divMsg = $('#divMsg').text()
    setTimeout(() => {
        // alert("MESSAGE TIMEOUT", divMsg
        $('#divMsg').slideUp()
    }, 2000)
})

// for getting url after applying ordering
function finalurl() {
    var url = new URL(window.location.href);
    var search_params = url.searchParams;
    search_params.set('showEntries', $('#showEntries').val());
    url.search = search_params.toString();
    var new_url = url.toString();
    return new_url
}

function showEntriesVal(name) {
    if (name = (new RegExp('[?&]' + encodeURIComponent(name) + '=([^&]*)')).exec(location.search))  //location.search give query sling part
        return decodeURIComponent(name[1]);
}

if (showEntriesVal('showEntries')) {
    console.log(showEntriesVal('showEntries'));
    $('#showEntries').val(showEntriesVal('showEntries'))
    // document.getElementById('placeholder').innerHTML = "Sort: " + document.getElementById(get('ordering')).innerHTML;
}


// FOR SIDE FOR AND SIDE BAR INNER OPTIONS::::::
$('.sideShow1').on("click", () => {
    console.log('sdf');
    $('.sideShow1 ul').toggleClass('side_show')
})

$('.sideShow2').on("click", () => {
    $('.sideShow2 ul').toggleClass('side_show')
})

$('#sidebarToggle').click(() => {
    console.log('asdfd');
    $("#sidebarID").toggleClass("sidebar-show");
    // $('#sideNavTogglebtn li span' ).toggleClass('sidebar_click fa-align-left fa-xmark ')
    // $('#sideNavTogglebtn' ).toggleClass('toggleBtn')
    $("#content-wrapper").toggleClass('content-click')
    // $('#bodyID').toggleClass('content-set')
})

// REGISTER PAGE NAME ERROR
setTimeout(function () { if ($('#paraRegNameError').length > 0) { $('#paraRegNameError').remove(); } }, 2000)

// Get the image and insert it inside the modal - use its "alt" text as a caption

function modalFeedImage(x) {
    var modal = document.getElementById("myModal");
    var img = document.getElementById(x);
    var modalImg = document.getElementById("img01");
    var captionText = document.getElementById("caption");
    modal.style.display = "block";
    modalImg.src = img.src;
    captionText.innerHTML = img.alt;
}

// Get the <span> element that closes the modal
// var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
// span.onclick = function () {
//     modal.style.display = "none";
// }

function CloseFeedImg() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
    // $('#myModal').attr('style', 'display: none;')
}
// END OF MODAL FEED IMAGE DISPLATT############

// OVERLAY DETAILS ON IMAGE::
function OverlayDetails(x) {
    x.attr('class', 'imgOverlay imgBlur')
}
function NormalDetails(x) {
    x.attr('class', '')
}

// BINDING USENAME TO NAVBAR input:hidden[name=]
username = $('#hiddenUserName').val()
if (username.length > 0) {
    // console.log("BINDING USENAME TO NAVBAR",username)
    $('#navbarUserName').text('Hi ' + username + '...')
}

// MESSAGE TIMEOUT
// divMsg=$('#divMsg').text()
// setTimeout(() => {
//     alert("MESSAGE TIMEOUT", divMsg)
//     if (divMsg.length > 0) {
//         $('#divMsg').slideUp()
//     }
// }, 2000)

// UNIQUE ID BINDING USING JS in REGISTRATION
function idForRejection(x) {
    $('#formRejectionReason').attr('action', '/approvereject/' + x + '/')
}

// DATA TABLE PULGIN CSS CONTROL:::
// $('#tableAdminControl_filter').attr('class', 'rounded form-control')

// IMAGE PREVIEW SCRIPT
$(document).ready(() => {
    // DATATABLE PLUGIN:
    $('#tableAdminControl').DataTable();
    // $('#tableAdminControl-2').DataTable();
    $('#tableAdminActioned').DataTable()

    // IMAGE PREVIEWERR
    $('#fileImage').change(function () {
        const file = this.files[0];
        console.log(file)
        if (file) {
            let reader = new FileReader();
            reader.onload = function (event) {
                $('#imgPreview').attr('src', event.target.result);
            };
            reader.readAsDataURL(file);
        }
        else {
            $("#imgPreview").attr("src", 'css/image/upload-image.jpg');
        }
    });

    // Dropify Image preview::::
    $('.dropify').dropify();

    // For pass url params for sorting table data:::
    var url = new URL(window.location.href);
    var search_params = url.searchParams;
    search_params.set('showEntries', $('#showEntries').val());
    url.search = search_params.toString();
    var new_url = url.toString();
    return new_url

});

// SEARCH BAR ON NAVBAR
$("#tableSearch").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#tableAddProduct tr").filter(function () {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
});



// $('#showEntries').on('change', ()=>{
//     ddVal = $('#showEntries').val()
//     console.log(ddVal);
//     $.ajax({
//         methode:'POST',
//         url:'http://127.0.0.1:8000/adminpage2/',
//         data:{'showEntries':ddVal,}
//     })
//     .done((data)=>{
//         // location.reload();
//         // console.log(data);
//     })
//     .fail((err)=>{
//         console.log(err);
//     })
// })
// SIDE BAR TOGGLE SCRIPT

(function ($) {

    "use strict";

    var fullHeight = function () {

        $('.js-fullheight').css('height', $(window).height());
        $(window).resize(function () {
            $('.js-fullheight').css('height', $(window).height());
        });

    };
    fullHeight();

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

})(jQuery);

// function ViewImageDetails(imgs) {
//     var expandImg = document.getElementById("feedImage");
//     var imgText = document.getElementById("imgtext");
//     expandImg.src = imgs.src;
//     imgText.innerHTML = imgs.alt;
//     expandImg.parentElement.style.display = "block";
// }

function ValidateRegister() {
    var name = $('#divRegisterName input').val()
    var email = $('#divRegisterEmail input').val()
    var pas1 = $('#divRegisterPassword input').val()
    var pas2 = $('#divRegisterConfirmPassword input').val()
    if (name == '') {
        alert("Name shouldn't be empty!!!")
        // $('#divRegisterName p').text("Name shouldn't be empty!!!")
        return false;
    }
    if (isNaN(name) == false) {
        alert("No numbers!!!")
        // $('#divRegisterName p').text("No numbers!!!")
        return false;
    }
    if (email == '') {
        // $('#divRegisterEmail p').text("Enter email!!!")
        alert("Enter email!!!")
        return false;
    }
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email) == false) {
        // $('#divRegisterEmail p').text("Enter valid email!!!") 
        alert("Enter valid email!!!")
        return false;
    }
    if (pas1 == '') {
        // $('#divRegisterPassword p').text("Enter password!!!")
        alert("Enter password!!!")
        return false;
    }
    if (pas2 == '') {
        // $('#divRegisterConfirmPassword p').text("Enter Confirm password!!!")
        alert("Enter Confirm password!!!")
        return false;
    }
    if (pas1 != pas2) {
        // $('#divRegisterPassword p').text("Password not matching!!!")
        alert("Password not matching!!!")
        return false;
    }
    else {
        return true
    }
}

// VALIDATE POST FORM::::
function ValidatePostForm() {
    let postname = $('#txtPostName').val()
    let img = $('#fileImage').val()
    var imgExten = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
    if (postname == '') {
        // $('#paraPostName').text('Post name is empty!!!')
        alert("Post name is empty!!!")
        return false;
    }
    if (img == '') {
        // $('#paraPostImage').text('Upload Image!!!')
        alert("Upload Image!!!")
        return false;
    }
    if (!imgExten.exec(img)) {
        // $('#paraPostImage').text('Invalid file type!!!')
        alert("Invalid file type!!!")
        return false;
    }
    else {
        return true;
    }
}


// SORTING TABLE DATA:::
var properties = [
    'tableSno',
    'tablePostName',
    'tableDescription',
    'tableStatus',

];

$.each(properties, function (i, val) {

    var orderClass = '';

    $("#" + val).click(function (e) {
        e.preventDefault();
        $('.filter__link.filter__link--active').not(this).removeClass('filter__link--active');
        $(this).toggleClass('filter__link--active');
        $('.filter__link').removeClass('asc desc');

        if (orderClass == 'desc' || orderClass == '') {
            $(this).addClass('asc');
            orderClass = 'asc';
        } else {
            $(this).addClass('desc');
            orderClass = 'desc';
        }

        var parent = $(this).closest('.header__item');
        var index = $(".header__item").index(parent);
        var $table = $('.table-content');
        var rows = $table.find('.table-row').get();
        var isSelected = $(this).hasClass('filter__link--active');
        var isNumber = $(this).hasClass('filter__link--number');

        rows.sort(function (a, b) {

            var x = $(a).find('.table-data').eq(index).text();
            var y = $(b).find('.table-data').eq(index).text();

            if (isNumber == true) {

                if (isSelected) {
                    return x - y;
                } else {
                    return y - x;
                }

            } else {

                if (isSelected) {
                    if (x < y) return -1;
                    if (x > y) return 1;
                    return 0;
                } else {
                    if (x > y) return -1;
                    if (x < y) return 1;
                    return 0;
                }
            }
        });

        $.each(rows, function (index, row) {
            $table.append(row);
        });

        return false;
    });

});



// setTimeout(()=>{
//     if ($('#formRegister p').length > 0){
//         $('#formRegister p').remove()
//     }
// },4000)

// function ValidateRegisterName(x)
// if (x=""){
//     text = 'Username should be filled!!!'
//     return false;
// }
// if (isNaN(x)){
//     text = 'No numbers!!!'
//     return false;
// }
// if (x.length > 50){
//     text = 'Username should be short!!!'
//     return false;
// }
// else{
//     done = 'ok'
// }
// $('#divRegisterName').text(text)
// $(document).ready(){

// }




// function paginatioCount() {
//     var data = $('#showEntries').val()
//     $.ajax({
//         methode: 'POST',
//         url: 'http://127.0.0.1:8000/adminpage2/',
//         data: {'showEntries': data}
//     })
// }
// <select name="showEntries" id="showEntries" onchange="paginatioCount()"></select>

// print(request.GET.get('showEntries'))