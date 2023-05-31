import { AdvertisementTypeEnum, AdvertisementUrgencyEnum } from '@/types/advertisementTypes';

export type ApiAdvertisementImageType = {
  url: string;
};

export type ApiAdvertisementCategoryType = {
  id: number;
  title: string;
};

export type ApiAdvertisementType = {
  id: number;
  title: string;
  description: string;
  advertisement_type: AdvertisementTypeEnum[];
  images: ApiAdvertisementImageType[];
  urgency_type: AdvertisementUrgencyEnum;
  category: ApiAdvertisementCategoryType;
};

export type ApiAdvertisementListItemType = {
  id: number;
  title: string;
  description: string;
  advertisement_type: AdvertisementTypeEnum[];
  images: ApiAdvertisementImageType[];
  urgency_type: AdvertisementUrgencyEnum;
  category: ApiAdvertisementCategoryType;
};

export type ApiPatchedAdvertisementType = {
  id: number;
  title?: string;
  description?: string;
  advertisement_type?: AdvertisementTypeEnum[];
  images?: ApiAdvertisementImageType[];
  urgency_type?: AdvertisementUrgencyEnum;
  category?: ApiAdvertisementCategoryType;
};

export type ApiCreatedAdvertisementType = {
  title: string;
  description: string;
  advertisement_type: AdvertisementTypeEnum[];
  images?: File[];
  urgency_type: AdvertisementUrgencyEnum;
  category: number;
};
