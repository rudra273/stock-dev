from rest_framework import serializers

class StockDataSerializer(serializers.Serializer):
    Symbol = serializers.CharField()
    Open = serializers.FloatField()
    High = serializers.FloatField()
    Low = serializers.FloatField()
    Close = serializers.FloatField()
    CurrentPrice = serializers.FloatField()
    PreviousClose = serializers.FloatField()
    FiftyTwoWeekLow = serializers.FloatField()
    FiftyTwoWeekHigh = serializers.FloatField()
    WeeklyLow = serializers.FloatField()
    WeeklyHigh = serializers.FloatField()
    MonthlyLow = serializers.FloatField()
    MonthlyHigh = serializers.FloatField()
    MarketCap = serializers.IntegerField(allow_null=True)
    CompanyName = serializers.CharField() 
    Currency = serializers.CharField()
    PercentageChange = serializers.FloatField()
    PriceChange = serializers.CharField()
    MarketState = serializers.CharField()


class HistoricalStockDataSerializer(serializers.Serializer):
    Date = serializers.DateTimeField()  
    Close = serializers.FloatField() 

