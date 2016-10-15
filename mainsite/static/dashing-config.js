/* global $, Dashboard */

var dashboard = new Dashboard();

dashboard.addWidget('clock_widget', 'Clock');

dashboard.addWidget('article_count', 'Number', {
    getData: function () {
        var self = this;
        $.get('widgets/article_count/', function(scope) {
            $.extend(self.scope, scope);
        });
    },
    interval: 5000
});

dashboard.addWidget('brief_count', 'Number', {
    getData: function () {
        var self = this;
        $.get('widgets/brief_count/', function(scope) {
            $.extend(self.scope, scope);
        });
    },
    interval: 5000
});

dashboard.addWidget('top_articles', 'List', {
    row: '2',
    col: '3',
    getData: function () {
        var self = this;
        $.get('widgets/top_articles/', function(scope) {
            $.extend(self.scope, scope);
        });
    },
    interval: 5000
});

dashboard.addWidget('top_briefs', 'List', {
    row: '2',
    col: '3',
    getData: function () {
        var self = this;
        $.get('widgets/top_briefs/', function(scope) {
            $.extend(self.scope, scope);
        });
    },
    interval: 5000
});

