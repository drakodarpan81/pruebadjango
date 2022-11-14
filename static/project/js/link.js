$(document).ready(function(){
    $("input\[type='number'\]").inputSpinner();

    // Vanilla JS
    const td = new tempusDominus.TempusDominus(document.getElementById('datetimepicker1'));
    td.dates.formatInput = function(date) { {return moment(date).format('DD/MM/YYYY HH:mm') } }

    new tempusDominus.TempusDominus(document.getElementById('datetimepicker1'), {
        localization: {
            dayViewHeaderFormat: { month: 'long', year: '2-digit' },
            locale: 'es',
            startOfTheWeek: 0
        },
    });
});