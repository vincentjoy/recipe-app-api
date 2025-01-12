"""Serializers for recipe APIs"""

from rest_framework import serializers

from core.models import (
    Recipe,
    Tag,
    Ingredient,
)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredients."""

    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ['id']


class TagSerializer(serializers.ModelSerializer): # this should be here (above RecipeSerializer) because RecipeSerializer has TagSerializer needed inside it
    """Serializer for tags."""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer): # Using model serializer here because this serializing is going to represent a specific model
    """Serializer for recipes."""
    tags = TagSerializer(many=True, required=False) # required=False makes the tags field in Recipe as an optional field
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'time_minutes', 'price', 'link', 'tags',
            'ingredients',
        ]
        read_only_fields = ['id']

    def _get_or_create_tags(self, tags, recipe): # this is needed because in nested serializer, those are read only, means tags will be a read only field in recipe. But we have to create tags along with recipe, so we need to override this default implementation
        """Handle getting or creating tags as needed."""
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create( # get_or_create is a helper method which gets the value if it already exists or if it doesn't exist, it creates a value with the values
                user=auth_user,
                **tag, # **tag is the way we are future proofing the tags field, so if ever other fields get added to tags, other than name, then that also will get accepted here
            )
            recipe.tags.add(tag_obj)

    def _get_or_create_ingredients(self, ingredients, recipe):
        """Handle getting or creating ingredients as needed."""
        auth_user = self.context['request'].user
        for ingredient in ingredients:
            ingredient_obj, created = Ingredient.objects.get_or_create( # get_or_create is a helper method which gets the value if it already exists or if it doesn't exist, it creates a value with the values
                user=auth_user,
                **ingredient,
            )
            recipe.ingredients.add(ingredient_obj)

    def create(self, validated_data):
        """Create a recipe."""
        tags = validated_data.pop('tags', []) # tags cannot be directly send to recipe creation method, because recipe model is expecting only values for the recipe and it expects tags to be assigned as a relational field. So we have to first pop it from the validated_data to have it later assigned seperately
        ingredients = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)
        self._get_or_create_ingredients(ingredients, recipe)

        return recipe

    def update(self, instance, validated_data): # since we are doing update, we get the existing instance, which is an object of Recipe
        """Update recipe."""
        tags = validated_data.pop('tags', None)
        ingredients = validated_data.pop('ingredients', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)
        if ingredients is not None:
            instance.ingredients.clear()
            self._get_or_create_ingredients(ingredients, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class RecipeDetailSerializer(RecipeSerializer): # RecipeSerializer is the base class because we want all the functionalities and fields of RecipeSerializer, plus some additional fields, thus avoiding code duplication
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']


class RecipeImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to recipes."""

    class Meta:
        model = Recipe
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}