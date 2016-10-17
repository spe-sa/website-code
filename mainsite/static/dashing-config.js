/* global $, Dashboard */

var myDashboardSet = new DashboardSet({
    rollingChoices: true,
});

myDashboardSet.addAction('Go to Google', function() { window.location.href = 'https://google.com/';
})

dashboard = myDashboardSet.addDashboard('main');

dashboard.addWidget('top_5_articles', 'List', {
    row: '1',
    col: '3',
    getData: function () {
        var self = this;
        $.get('widgets/top_5_articles/', function(scope) {
            $.extend(self.scope, scope);
        });
    },
    interval: 6000000
});

dashboard.addWidget('clock_widget', 'Clock');

dashboard.addWidget('article_count', 'Number', {
    getData: function () {
        var self = this;
        $.get('widgets/article_count/', function(scope) {
            $.extend(self.scope, scope);
        });
    },
    interval: 6000000
});

dashboard.addWidget('brief_count', 'Number', {
    getData: function () {
        var self = this;
        $.get('widgets/brief_count/', function(scope) {
            $.extend(self.scope, scope);
        });
    },
    interval: 6000000
});

dashboard.addWidget('top_5_briefs', 'List', {
    row: '1',
    col: '3',
    getData: function () {
        var self = this;
        $.get('widgets/top_5_briefs/', function(scope) {
            $.extend(self.scope, scope);
        });
    },
    interval: 6000000
});

dashboard = myDashboardSet.addDashboard('articles');
dashboard.addWidget('top_20_articles', 'List', {
    row: '2',
    col: '3',
    getData: function () {
        var self = this;
        $.get('widgets/top_20_articles/', function(scope) {
            $.extend(self.scope, scope);
        });
    },
    interval: 6000000
});

dashboard = myDashboardSet.addDashboard('briefs');
dashboard.addWidget('top_20_briefs', 'List', {
    row: '2',
    col: '3',
    getData: function () {
        var self = this;
        $.get('widgets/top_20_briefs/', function(scope) {
            $.extend(self.scope, scope);
        });
    },
    interval: 6000000
});
