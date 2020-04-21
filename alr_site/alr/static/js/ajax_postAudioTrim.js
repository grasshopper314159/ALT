function create_post() {
    console.log("create post is working!") // sanity check
    //console.log($('#trimAudioForm').val())

    $.ajax(
        {
        type: 'POST',
        data: {
            'bigAudioUrl':bigAudioUrl,
            'boxlist': JSON.stringify(drawBoxList),
            "trimLength":document.getElementById("trimLength"),
            "formStartTime":document.getElementById("formStartTime"),
            "english_text":document.getElementById("english_text"),
            "original_text":document.getElementById("original_text")

        },
        url: "/ajax/postTrimAudio/",

        success: function(response)
        {
            // ViewAudio.html table body has id='data'
            data = document.getElementById('data');

            for (var key in response) {
                console.log(key);
            }

            // entry = '<tr><td>' +
            //     '<div class="w3-bar">' +
            //     '<button class="w3-button w3-tiny w3-white w3-border w3-round">Edit</button>'+
            //     '<button class="w3-button w3-tiny w3-white w3-border w3-round">Del</button>'+
            //     '</div></td>' +
            //     '<td>' + response[key]['owner'] + '</td>' +
            //     '<td>' + response[key]['speaker'] + '</td>' +
            //     '<td>' + response[key]['original_text'] + '</td>' +
            //     '<td>' + response[key]['english_text'] + '</td>' +
            //     '<td>' + response[key]['score'] + '</td>' +
            //     '<td>' + response[key]['date'] + '</td>' +
            //     '<td><audio controls><source src="' + response[key]['url'] + '" type="audio/wav">Your browser does not support the audio element.</audio>' +
            //     '<td><button class="w3-btn w3-white w3-block w3-border w3-round" onclick="showTrimDetails(\'id\');">Show</button>' +
            //     '</td></tr>';
            // data.innerHTML += entry;
            }
            // TODO: use localStorage to save reaponse for later?
            // localStorage.setS

        },

        failure: function()
        {
            alert("AJAX FAILED!");
        }
        }
    );
};



