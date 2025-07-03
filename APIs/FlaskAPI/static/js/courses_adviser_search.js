$(document).ready(function () {
    console.log('Document is ready.');

    $('#courserAdvicer-search').on('input', function () {
        console.log('Input event triggered.');

        var searchValue = $(this).val().toLowerCase();

        $('.content-container').each(function () {
            var courseText = $(this).text().toLowerCase();

            console.log(`Course Text: ${courseText}, Search Value: ${searchValue}`);

            if (courseText.includes(searchValue)) {
                console.log('Match found. Showing element.');
                $(this).closest('.row').show();
            } else {
                console.log('No match. Hiding element.');
                $(this).closest('.row').hide();
            }
        });
    });
});