// textbox for manual entry of role must be hidden by default
//$("#id_role").parents('div').hide()
// textbox for manual entry of institution must be hidden by default
$("#id_institution").parents('div').hide()
// textbox for manual entry of reason must be hidden by default
$("#id_reason").parents('div').hide()

//var checkBox = document.getElementById("id_nightstay");
//var chosen_role = document.getElementById("id_role_dropdown")
var chosen_institution = document.getElementById("id_institution_dropdown")
var chosen_reason = document.getElementById("id_reason_dropdown")
//var role_text = chosen_role.options[chosen_role.selectedIndex].text
var institution_text = chosen_institution.options[chosen_institution.selectedIndex].text
var reason_text = chosen_reason.options[chosen_reason.selectedIndex].text
// id_role always has a copy of the data chosen from the dropdown
//document.getElementById("id_role").value = role_text
// id_institution always has a copy of the data chosen from the dropdown
document.getElementById("id_institution").value = institution_text
// id_reason always has a copy of the data chosen from the dropdown
document.getElementById("id_reason").value = reason_text
// called each time there a different option in the role dropdown is chosen
//$("#id_role_dropdown").change(function () {
//    role_text = chosen_role.options[chosen_role.selectedIndex].text
    // id_role stores the data from the dropdown
//    document.getElementById("id_role").value = role_text
    // id_role is made visible so user can manually enter their role
//    if (chosen_role.value === 'other') {
//        $("#id_role").parents('div').show()
//        document.getElementById("id_role").value = ''
//        document.getElementById("id_role").placeholder = 'Explain your Role'
//    }
//    else {
//        $("#id_role").parents('div').hide()
//    }
//
//})

// called each time there a different option in the institution dropdown is chosen
$("#id_institution_dropdown").change(function () {
    institution_text = chosen_institution.options[chosen_institution.selectedIndex].text
    // id_institution stores the data from the dropdown
    document.getElementById("id_institution").value = institution_text
    // id_institution is made visible so user can manually enter their institution
    if (chosen_institution.value === 'other') {
        $("#id_institution").parents('div').show()
        document.getElementById("id_institution").value = ''
        document.getElementById("id_institution").placeholder = 'Institusi Anda'
    }
    else {
        $("#id_institution").parents('div').hide()
    }

})

$("#id_reason_dropdown").change(function () {
    reason_text = chosen_reason.options[chosen_reason.selectedIndex].text
    // id_reason stores the data from the dropdown
    document.getElementById("id_reason").value = reason_text
    // id_reason is made visible so user can manually enter their role
    if (chosen_reason.value === 'other') {
        $("#id_reason").parents('div').show()
        document.getElementById("id_reason").value = ''
        document.getElementById("id_reason").placeholder = 'Kegiatan Anda'
    }
    else {
        $("#id_reason").parents('div').hide()
    }

})
// storing current date and time
var today = new Date();
var day = today.getDate()
// if it is after 5pm then set the default checkout date as the next day
if (today.getHours() >= 17) {
    day = today.getDate() + 1
}

// rearranging the date and time as per the required format
var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + day;
var time = "17" + ":" + "00" + ":" + "00"
var dateTime = date + 'T' + time;

document.getElementById("id_planned_checkout").value = dateTime

// detecting if the browser is chrome/firefox/safari
let f = navigator.userAgent.search("Firefox");
let s = navigator.userAgent.search("Safari");
let c = navigator.userAgent.search("Chrome");

// use default chrome datetime picker if chrome
if (c > -1) {
    c = 1
}
// use flatpicker custom datetime picker if firefox
else if (f > -1) {
    config = {
        enableTime: true,
        enableSeconds: false,
        dateFormat: "Y-m-d H:i:s",
    }
    flatpickr("input[type=datetime-local]", config);
}
// use flatpicker custom datetime picker if safari
else if (s > -1) {
    config = {
        enableTime: true,
        enableSeconds: false,
        dateFormat: "Y-m-d H:i:s",
    }
    flatpickr("input[type=datetime-local]", config);
}

// clicking of the nightstay checkbox hides/unhides the emergency section
//$("#id_nightstay").click(function () {
//    var checkBox = document.getElementById("id_nightstay");
//   if (checkBox.checked === true) {
//        $("#id_emergency_first_name").parents('div').show()
//        $("#id_emergency_last_name").parents('div').show()
//        $("#id_emergency_phone").parents('div').show()
//        $("#id_emergency_relation").parents('div').show()
//    }
//    if (checkBox.checked === false) {
//        $("#id_emergency_first_name").parents('div').hide()
//        $("#id_emergency_last_name").parents('div').hide()
//        $("#id_emergency_phone").parents('div').hide()
//        $("#id_emergency_relation").parents('div').hide()
//    }
//})

// this is mainly to prevent page from resetting when it is reloaded
//if (chosen_role.value === 'other') {
//    $("#id_role").parents('div').show()
//    document.getElementById("id_role").value = ''
//    document.getElementById("id_role").placeholder = 'Explain your Role'
//}
if (chosen_institution.value === 'other') {
    $("#id_institution").parents('div').show()
    document.getElementById("id_institution").value = ''
    document.getElementById("id_institution").placeholder = 'Institusi Anda'
}
if (chosen_reason.value === 'other') {
    $("#id_reason").parents('div').show()
    document.getElementById("id_reason").value = ''
    document.getElementById("id_reason").placeholder = 'Kegiatan Anda'
}
// this is mainly to make sure page acts appropriately when reloaded
//if (checkBox.checked === false) {
//    $("#id_emergency_first_name").parents('div').hide()
//    $("#id_emergency_last_name").parents('div').hide()
//    $("#id_emergency_phone").parents('div').hide()
//    $("#id_emergency_relation").parents('div').hide()
//}



