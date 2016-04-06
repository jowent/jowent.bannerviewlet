#! /bin/sh

I18NDOMAIN="jowent.bannerviewlet"

# Check if manual overrides exist
if test -e locales/manual.pot; then
        echo "Manual PO entries detected"
        MERGE="--merge locales/manual.pot"
else
        echo "No manual PO entries detected"
        MERGE=""
fi

# Synchronise the templates and scripts with the .pot.
# All on one line normally:
i18ndude rebuild-pot --pot locales/${I18NDOMAIN}.pot \
    $MERGE \
    --create ${I18NDOMAIN} \
   .

# Synchronise the resulting .pot with all .po files
for po in locales/*/LC_MESSAGES/${I18NDOMAIN}.po; do
    i18ndude sync --pot locales/${I18NDOMAIN}.pot $po
done
